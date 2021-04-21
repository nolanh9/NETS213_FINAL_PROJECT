import pandas as pd
import csv

def QC(raw_results):
    # filter for workers who have gotten obvious questions wrong 
    bad_workers = raw_results[(raw_results["Answer.QC_liberal"] != "Liberal") | (raw_results["Answer.QC_conservative"] != "Conservative") | (raw_results["Answer.QC_neither"] != "Neither")]
    # gather worker ids into set
    return set(bad_workers["WorkerId"].unique())


# workers_to_kick: output of QC, list of workers with results we should throw out
# raw_results: data from mturk
# returns tweets mapped to their average rating (input into classifier training)
def aggregation(workers_to_kick, raw_results):
    #take out ratings using QC output
    scores = raw_results[~raw_results['WorkerId'].isin(workers_to_kick)]
    
    # COMMENT THIS FILTER BACK IN WHEN WE HAVE MORE DATA (REAL DATASET)
    # throw out results that have less than 3 ratings
    # scores = scores[scores['Input.Tweet'].isin(scores['Input.Tweet'].value_counts()[scores['Input.Tweet'].value_counts()>2].index)]
    
    #normalize by political party
    scores.loc[scores['Answer.Label'] == "Liberal", 'Answer.Extreme'] += 10

    #get average scores of each tweet 
    return scores.groupby('Input.Tweet')['Answer.Extreme'].mean()

def run_experiment(csv_path):
    mturk_df = pd.read_csv(csv_path)
    display(mturk_df)
    bad_workers = QC(mturk_df)
    with open('qc_output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(list(bad_workers))
    tweet_ratings = aggregation(bad_workers, mturk_df)
    tweet_ratings.to_csv('aggregation_output.csv')
    return tweet_ratings

CSV_FILE_PATH = "toy_dataset_final.csv"
display(run_experiment(CSV_FILE_PATH))