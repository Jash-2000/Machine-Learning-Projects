# The UNSW-NB15 data set

Implementation of a basic deep neural network for network packet classification using Tensorflow.

Link to description of dataset: https://www.unsw.adfa.edu.au/australian-centre-for-cyber-security/cybersecurity/ADFA-NB15-Datasets/

The code can be seen as a learning example on how to build a neural network using **Tensorflow** while preprocessing data with **Pandas** and **Numpy**.

---

## Details

The UNSW dataset contains 42 Features for each network packet, one label describing
if it is malicious or normal, and a category which can be any of the 10 types: Fuzzers,
Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms
and Normal.

Of the 42 features, 3 of them are categorical features (proto, service and state)
which need to be encoded into numbers so that they can be analysed to make
predictions. For this we use Pandas’s get_dummies() function, which creates new
dummy columns for each categorical feature. Due to this expansion, we now
have 196 features to work with.