#!/usr/bin/env python
# coding: utf-8


import pandas as pd
pred_out = pd.read_csv("prediction_output_soil1235seq.tsv",  sep= "\t")
pred_out["Truth_label"]=pred_out["Name"].str.split("|").str.get(0)
pred_out["Predict_label"]=pred_out["Type"].str.split("_").str.get(1)
pred_out["Predict_label_clean"] = pred_out["Predict_label"].replace({"aac3_1":"aac3", "aac3_2":"aac3", "blab1":"blab", "blab3":"blab", "dfra":"dfrA",})
filtered = pred_out.loc[pred_out.response == "Ref"]
score_df = filtered[["Sequence", "Name", "Truth_label", "Predict_label_clean"]]
off_target = len(score_df.loc[score_df.Truth_label != score_df.Predict_label_clean])
on_target = len(score_df.loc[score_df.Truth_label == score_df.Predict_label_clean])
nr_seq = pred_out.shape[0]
nr_seq_ref = score_df.shape[0]
score = (on_target / nr_seq)
not_ref_seq = (nr_seq - nr_seq_ref)
score_ref = (on_target / (on_target + off_target))
with open("score.txt", "w") as f:
    f.write("The ratio of on target sequences by the total number of sequences is\t%s\nThe number of sequences wrongly not classified as an ARDs is\t%s\nThe ratio of on target sequences among the one classified as ARDs is\t%s\n"%(str(score),str(not_ref_seq),str(score_ref)))
    
print("The ratio of on target sequences by the total number of sequences is\t%s\nThe number of sequences wrongly not classified as an ARDs is\t%s\nThe ratio of on target sequences among the one classified as ARDs is\t%s\n"%(str(score),str(not_ref_seq),str(score_ref)))
