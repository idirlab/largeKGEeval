## Inadequacy of Evaluation Metrics

### Closed-World Assumption
For this experiment, we need to extract a subset of the graph to train the models on and then evaluate them on the whole grand truth. For this part, we have a script to extract the subgraph of a favorable size. 

### Global Metrics
Global metrics focus on how to aggregate or report the results. We need to output the results on each test triple separately and then process them. For Macro-averaging by relation or domain and N-ary vs. binary relations, this is the case. However, for the Left vs. right entity link prediction, we need to report the results separately. (Please see the modified general_models.py file in the DGL-KE framework.) 

## Problems of the Generic Evaluation Protocol

### Link Prediction 
We conducted link prediction experiments using the four aforementioned KGE models in the DGL-KE framework on datasets FB-CVT-REV, FB+CVT-REV, and FB15k-237. We used the hyperparameters suggested in DGL-KE with some tweaks. The scripts and logs of our training are available in the folder logs.

### Other Evaluation Protocols
For Entity-Pair Ranking, Property Prediction, and Triple Classification, we have explained in detail how to perform the experiments in our manuscript. (Please see the modified general_models.py file in the DGL-KE framework.) 

