# On Large-Scale Evaluation of Embedding Models for Knowledge Graph Completion

## Overview
This work makes the following contributions
- We present a comprehensive large-scale evaluation of knowledge graph embedding models on FB-CVT-REV and FB+CVT-REV datasets.
- We provide quantitative results indicating that widely used evaluation metrics for knowledge graph embedding models, such as Mean Rank (MR) and Mean Reciprocal Rank (MRR), are based on the closed-world assumption, and they underestimate models' accuracy.
- We develop comprehensive global metrics revealing hidden performance patterns, including macro-averaging by relation or domain, analysis of left and right entity link predictions, and quantitative evidence showing how n-ary to binary conversion leads to overestimation of model performance.
- We highlight the limitations of link prediction as an evaluation protocol for knowledge graph embedding models, providing quantitative results underscoring the need for diverse evaluation protocols, and demonstrate how dataset size affects model performance and relative rankings among different KGE approaches.
- We introduce a new evaluation protocol, property prediction, and evaluate the knowledge graph embedding models on this protocol, entity-pair ranking, and triple classification as alternatives to link prediction.
  
## Datasets used 

We perform our experiments on two large-scale datasets, FB-CVT-REV and FB+CVT-REV. While FB+CVT-REV represents n-ary relationships using CVT nodes, FB-CVT-REV converts n-ary relationships into binary ones, similar to FB15k-237. This distinction allows us to assess how knowledge graph embedding model performance varies when data is modeled differently. These datasets, derived from Freebase, are large-scale, represent real-world scenarios, and do not include the data redundancy that exists in FB15k. **The dataset can be downloaded from this [link](https://zenodo.org/records/7909511).**

### Dataset Statistics

<table class="tg">
<thead>
  <tr>
    <th class="tg-fymr">variant</th>
    <th class="tg-7btt">CVT nodes</th>
    <th class="tg-7btt">reverse triples</th>
    <th class="tg-7btt">#entities</th>
    <th class="tg-7btt">#properties</th>
    <th class="tg-7btt">#triples</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">FB-CVT-REV</td>
    <td class="tg-c3ow">removed</td>
    <td class="tg-c3ow">removed</td>
    <td class="tg-c3ow">46,069,321</td>
    <td class="tg-c3ow">3,055</td>
    <td class="tg-c3ow">125,124,274</td>
  </tr>
  <tr>
    <td class="tg-0pky">FB+CVT-REV</td>
    <td class="tg-c3ow">retained</td>
    <td class="tg-c3ow">removed</td>
    <td class="tg-c3ow">59,894,890</td>
    <td class="tg-c3ow">2,641</td>
    <td class="tg-c3ow">134,213,735</td>
  </tr>
</tbody>
</table>

## Experiments & Results

To perform the experiments in this paper, we utilized the provided training, validation, and test sets of the FB-CVT-REV and FB+CVT-REV datasets, with the split ratio of 90/5/5. Our experiments were conducted on an NVIDIA H100 80GB GPU. We also extend our gratitude to the Texas Advanced Computing Center (TACC) for providing computing resources used in this work’s experimentation. We trained all the models, TransE, DistMult, ComplEx, and RotatE, using the DGL-KE framework ([Zheng et al.,2020](https://arxiv.org/pdf/2004.08532.pdf)). Our scripts and the version of DGL-KE used for this work are available in this repository. 

## Related Work
Please feel free to check out other papers of ours related to this topic: 
- [Comprehensive analysis of freebase and dataset creation for robust evaluation of knowledge graph link prediction models](https://drive.google.com/file/d/1evfTheEJ4jVsjvXB-BRj9FE13UmtiQap/view)
- [Realistic re-evaluation of knowledge graph completion methods: An experimental study](https://dl.acm.org/doi/pdf/10.1145/3318464.3380599)


## License

The dataset and code are made available under the [CC0 1.0 Universal](https://github.com/idirlab/largeKGEeval/blob/main/LICENSE).
