<div style="text-align: center;">

# Apache SkyWalking - AIOps Log clustering with Flink (Algorithm Optimization)

## Proposal for Google Summer of Code 2023

</div>

## Personal Information

**Name** Shuanglong Zhu

**Email** Sheltonzsl123@gmail.com

**GitHub** https://github.com/SheltonZSL

**University** Queen's University, ON, Canada

**Time Zone** GMT-4

## About me & Why Me?

I am a 2nd-year undergraduate student in the Department of Computing at Queen's University in Canada. During my freshman
year, I was not a computer science student but was involved in a university course in computing because of my personal
interest. I entered the computing program this year because I was very interested in computers. After my first ever
countering with Python, my love for computer science start to grow. Currently, my programming skills cover Python and
Java. During the free time beyond coursework, I taught myself database design and learnt PostgreSQL. I also followed
online tutorial and developed a scraper & website, both deployed with Docker.

The reason why I'm genuinely interested this project is that I am ??? in SkyWalking and Flink. I had made some
contributions to SkyWalking before and briefly understood the project content of SkyWalking. I want to contribute more
to the SkyWalking's project. As for Flink, a distributed processing engine, I have familiarized myself with its
applications before. It can help SkyWalking to process user log files very well. But processing these log files and
displaying them better requires a robust algorithm. In this case, we have investigated and targeted a state-of-the-art
algorithm namely Drain3, and I think it's a good fit for my GSoC project. Therefore, I consider myself a good fit for
this SkyWalking Flink project. I am looking forward to working with the SkyWalking community.

## Project Description

- **Project Name**: [Apache SkyWalking - AIOps Log clustering with Flink (Algorithm Optimization)](https://issues.apache.org/jira/browse/GSOC-107)

- **Mentors**:
    - [@wu-sheng](https://github.com/wu-sheng)
    - [@Superskyyy](https://github.com/Superskyyy)
- **Abstract**: SkyWalking can freely export log messages from its storage and send them to third-party for long-term
  storage and analysis. Although the current SkyWalking engine is able to auto correlate logs, traces and metrics, while
  also supporting analyzing logs through a Domain Specific Language (DSL) called "Log Analysis Language (LAL)", it
  depends heavily on the fact that the user must comprehend the contents of the incoming logs, and must be able to
  precisely define the log analysis rules. This is not always the case. In many cases, the user may not be able to
  understand the contents of the log, or may not be able to define the log analysis rules precisely. In this case,
  SkyWalking needs to provide a more intelligent log analysis method. In this project, we will use Flink to implement
  the Drain3 algorithm to automatically cluster similar log messages together and generate a template for each cluster.
  The log messages are not processed during this process. Flink can help Kafka perform real-time stream processing and
  process unbounded stream log information in this process. The algorithm part of Flink that needs to be implemented in
  the project is Drain3.

- **Goal**:
    - Complete the algorithm model of applying Drain3 in Flink.
    - Test and optimize the Drain3 algorithm based on real-world datasets and incorporate user feedback.

## Background

### What is AIOps?

AIOps stands for Artificial Intelligence for IT Operations. It is a new technology that applies artificial intelligence
and machine learning to the IT operations field. AIOps can help enterprises better manage their IT infrastructure,
improve their operational efficiency and reliability. It can automate the monitoring, analysis and management of IT
systems, thereby improving the efficiency and accuracy of IT operations.

### SkyWalking and AIOps

The SKyWalking community would like to implement an practical AIOps engine robust, efficient and open-source for the era
of cloud computing. The AIOps engine can help with better observability and reliable reactive anomaly detection. It can
also help analyze log files and the relationship between logs and traces.

### The log clustering problem

This figure shows the relationship between AIops and SkyWalking[5].
[![img_1.png](img_1.png)](https://github.com/SkyAPM/aiops-engine-for-skywalking/blob/master/docs/static/log-trend-analysis-arch.png?raw=true)
SkyWalking processes log messages through the AIOps engine for log clustering. Log clustering is a significant part of
AIOps. When SkyWalkin implements this feature with AIOps, we can see what the clustering of logs looks like using the
Skywalking Booster UI. How to do that, I'll talk about that later.

### Why Choose Drain3

The advantage of the Drain3 algorithm is that it is an online log template miner that can extract templates (clusters)
from log message streams in time. rain avoids constructing very deep and unbalanced trees because its log group search
process is a fixed depth parse tree[7]. To evaluate whether the algorithm model
is good, it is judged by three points: 1. Accuracy 2. Robustness 3. Efficiency. The reason why Drain3 is chosen is that
it has an advantage in the accuracy and robustness of log processing. According to the paper "Tools and Benchmarks for
Automated Log Parsing", "Compared to other log parsers, Drain achieves relatively stable accuracy and shows its
robustness when changing volumes of logs. [1]". As seen from the figure below, the accuracy of Drain3 is very high and
robustness is very good, and it achieved high accuracy on 9 out of 16 datasets, indicating that Drain3 is more general
and accurate.

![180ebaf497e71419ca6e897a16acd1f](https://user-images.githubusercontent.com/113407151/228029026-5f1b0aff-18f2-467c-a907-5ef07172a321.png)
![fc0c41cee326b39b47121412571bb7e](https://user-images.githubusercontent.com/113407151/228029051-4743cc07-fb27-4917-b766-385ac2f2ccca.png)

SkyWalking focus on robustness and accuracy, and Drain3 fit the current condition that SkyWalking need. I said that
because SkyWalking has many users, it needs a more general model to work the user's environment while keeping good
accuracy.

### Model of Drain3 (https://github.com/logpai/Drain3/blob/master/drain3/drain.py)

Based on the picture below, you can understand how Flink with Drain3 works.
![Flink and Drain3.png](..%2FFlink%20and%20Drain3.png)
Drain3 can extract templates (clusters) in time from Flink's log message stream. The principle
of Drain3 is based on Drain, which is an unsupervised log analysis method based on log messages. It can automatically
cluster similar log messages together and generate a template for each cluster. Drain3's message clustering is based on
the length of the log, which may have different lengths but the same log will not be clustered into a cluster. Besides,
the similarity calculation formula used in the original Drain3 implementation (not the Jaccard Drain implementation) is
as follows:

```text
sim = (Intersection of two logs(means log1=log2))/len(total log message)
```

This formula calculates the similarity between two sequences by dividing the length of their intersection by the length
of one of the sequences. However, this formula can greatly overestimate the similarity between two sequences, resulting
in overly simplified templates that look like this: "Log <>   <>   <>   <>   <>   <>   <>   <>   ".
To improve this formula, we can use a more accurate similarity measure such as Jaccard similarity. Jaccard similarity
measures the similarity between two sets by dividing the size of their intersection by the size of their union. This
measure can help to reduce overestimation and produce more accurate templates.

## Potential Enhancements to Investigate (Drain3)

**Jaccard Drain Evaluation:** Jaccard Drain is a recent enhancement merged into the Drain3 open-source algorithm
repository [3]. The same idea of enhancement also presents in the cited Huwei paper [1]. Jaccard Drain algorithm
utilizes the Jaccard similarity, a metric to measure the similarity between two sets. The Jaccard similarity of two sets
is defined as the size of the intersection divided by the size of the union of the two
sets. `J(A, B) = |A ∩ B| / |A ∪ B|`. The most important difference from naive similarity is that the Jaccard similarity
does not require both sets to present in the exact length. In reality, two logs of the same nature can vary in token
lengths, for example:

```text
Log1:Received disconnect from <:IP:>: <:NUM:>: <:*:> <:*:> <:*:>
Log2:Received disconnect from <:IP:>: <:NUM:>: <:*:> <:*:> <:*:> <:*:> <:*:> <:*:>
```

Since the Jaccard Drain algorithm is not been comprehensively evaluated yet, there remain tasks to fix a potential bug.
In the GSOC task, we plan to evaluate the Jaccard Drain algorithm against current public available log datasets on
LogHub [4], if it turns out to be effective, fast, and robust, we apply it in the Flink Workflow (it may or may not be
the default implementation).

**Dynamic Similarity Threshold and Depth**
The current implementation of Drain3 uses a fixed similarity threshold and depth. However, the similarity threshold and
depth can be dynamically adjusted based on the log volume and type. For example, if the log volume is low, the
similarity threshold can be set to higher to allow more logs to be grouped. If the log volume is high, the similarity
threshold can be set to a lower value to allow more records to be grouped. The same idea applies to depth. In the GSOC
task, we plan to implement a dynamic similarity threshold and depth adjustment mechanism in the Flink Workflow.

**Merge Log Groups**
When parameters are near the front and do not contain numbers, templates that should be identical may be split into
multiple templates. To solve this problem, we can make the following improvements to Drain. In all leaf nodes of the
same length partition tree, if there are templates whose similarity is greater than the specified threshold and whose
occurrence times are particularly low, these templates are merged and updated according to the steps of updating the
parse tree[5].

```text
temsim = lenLCS/min(lenNEW,lenEXIST)[2]
```

In the GSOC task, we plan to implement a merge log groups mechanism in the Flink Workflow.

# Plan

**TIMELINE**

Since the university vacation does not start until the beginning of May, I may need to delay the start of my project.

| Time                | Task                                                                                  |
|---------------------|---------------------------------------------------------------------------------------|
| Now - May 15st      | Familiarize myself with the project and the code base, and get to know the community. |
| May 15st - Jun 30th | Implement Drain3 apps in Flink                                                        |
| Jul 1st - Jul 31th  | Run a performance test with Drain3 Flink and Improve Drain3 model                     |
| Aug 1st - Aug 31th  | Connect with SkyWalking Flink and debug                                               |
| Sep 1st - Sep 10th  | Commit PR to Apache SkyWalking's code repository.                                     |

1. **Now - May 15st** :

- Get familiar with the project and learn more about Flink and Drain3.

- Look for the data set to use for the test

- Learn about Drain3 codebase and become familiar with its regular expressions.

2. **May 15st - Jun 30th**:

- implements Drain3 apps in Flink: I built the Drain3 base model and applied it to the original Flink. I will use the
  Flink's log message stream as the input of Drain3. The output of Drain3 is a template that can be used to identify
  similar log messages.


3. **Jul 1st - Jul 31th**:

- Run a performance test with Drain3 Flink: I will test Flink to build a good Drain algorithm using real life data sets[4]
  If the performance is not good enough, optimize the performance of Drain3 in Flink.


- Improved Drain3 algorithm shortcomings: I will improve the shortcomings of the Drain3 algorithm, such as the
  similarity calculation formula, the dynamic similarity threshold and depth, and the merge log groups.


4. **Aug 1st - Aug 31th**:

- Connect with SkyWalking Flink and debug: l will contact another SkyWalking Flink project participant, put the Drain3
  model into his project, and tweak it to fit.

5. **Sep 1st - Sep 10th**:

- Commit PR to Apache SkyWalking's code repository: submit a PR to Apache SkyWalking's code repository to add the Drain3
  algorithm to the SkyWalking Flink project.

- Provides the output and Drain3 algorithm test information: provide the output of the Drain3 algorithm and the test
  information of the Drain3 algorithm.

- Improve relevant documentation: improve the documentation of the Drain3 algorithm in the SkyWalking Flink project.

# Reference

[1] J. Zhu et al., "Tools and Benchmarks for Automated Log Parsing," 2019 IEEE/ACM 41st International Conference on
Software Engineering: Software Engineering in Practice (ICSE-SEIP), Montreal, QC, Canada, 2019, pp. 121-130, doi:
10.1109/ICSE-SEIP.2019.00021.

[2] He P, Zhu J, Xu P, Zheng Z, Lyu MR. A directed acyclic graph approach to online log parsing [Internet]. arXiv.org.
2018 [cited 2023Mar27]. Available from: https://arxiv.org/abs/1806.04356

[3] https://github.com/logpai/Drain3/blob/master/drain3/jaccard_drain.py

[4] https://github.com/logpai/loghub

[5] https://github.com/SkyAPM/aiops-engine-for-skywalking

[6] https://blog.csdn.net/pengzhouzhou/article/details/110211666

[7] He, Pinjia, et al. "Drain: An online log parsing approach with fixed depth tree." 2017 IEEE international conference
on web services (ICWS). IEEE, 2017.
