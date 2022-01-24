#!/usr/bin/env python
# coding: utf-8

import pandas as pd

tot_seq = int(input("Enter the number of the protein sequences contained in the dataset " ))
pred_out = pd.read_csv("prediction_output.tsv",  sep= "\t")
pred_out["Truth_label"]=pred_out["Name"].str.split("|").str.get(0)
pred_out["Predict_label"]=pred_out["Type"].str.split("_").str.get(1)
pred_out["Predict_label_clean"] = pred_out["Predict_label"].replace({"aac3_1":"aac3", "aac3_2":"aac3", "blab1":"blab", "blab3":"blab", "dfra":"dfrA",})
filtered = pred_out.loc[pred_out.response == "Ref"]
score_df = filtered[["Sequence", "Name", "Truth_label", "Predict_label_clean"]]
off_target = len(score_df.loc[score_df.Truth_label != score_df.Predict_label_clean])
on_target = len(score_df.loc[score_df.Truth_label == score_df.Predict_label_clean])
false_negatives = (tot_seq - on_target)
nr_seq = pred_out.shape[0]
nr_seq_ref = score_df.shape[0]
ignored = (tot_seq - nr_seq)
sensitivity = (on_target / tot_seq)
not_ref_seq = (tot_seq - nr_seq_ref)
score_ref = (on_target / (on_target + off_target))

with open("score.txt", "w") as f:
    f.write("The total number of sequences of the dataset (True positives + False negatives) is:\t%s\nThe number of on-target sequences (True positives) is:\t%s\nThe number of False negatives is:\t%s\nThe Sensitivity of the prediction (TP \ (TP+FN)) is:\t%s\n"%(str(tot_seq),str(on_target),str(false_negatives),str(sensitivity)))

print("The total number of sequences of the dataset (True positives + False negatives) is:\t%s\nThe number of on-target sequences (True positives) is:\t%s\nThe number of False negatives is:\t%s\nThe Sensitivity of the prediction (TP \ (TP+FN)) is:\t%s\n"%(str(tot_seq),str(on_target),str(false_negatives),str(sensitivity)))
