#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Can you think of a few applications for a sequence-to-sequence RNN? What about a sequence-to-vector RNN? And a vector-to-sequence RNN');get_ipython().run_line_magic('pinfo', 'RNN')

Ans: Sequence-to-Sequence RNN:

   Machine Translation
   Image Captioning
   Text Summarization

Sequence-to-Vector RNN:

   Speech Recognition
   Document Classification
   Sentiment Analysis
Vector-to-Sequence RNN:

   Music Generation
   Text Generation
   Generative Art
   
get_ipython().set_next_input('2. Why do people use encoder–decoder RNNs rather than plain sequence-to-sequence RNNs for automatic translation');get_ipython().run_line_magic('pinfo', 'translation')

Ans: Encoder–decoder RNNs are better suited for automatic translation than plain sequence-to-sequence RNNs because they are able 
to better capture the context of a sentence. An encoder–decoder RNN uses two separate recurrent neural networks, one to encode 
the source sentence into a fixed-length vector and the other to decode the fixed-length vector into a target sentence. This 
allows for more accurate translations because the context of the source sentence is better preserved.

get_ipython().set_next_input('3. How could you combine a convolutional neural network with an RNN to classify videos');get_ipython().run_line_magic('pinfo', 'videos')

Ans: A convolutional neural network combined with an RNN can be used to classify videos by first using the convolutional neural 
network to extract features from each frame of the video and then using the RNN to analyze the extracted features in order to 
classify the video as belonging to a certain class. The RNN will be able to look at the extracted features over a period of time 
and detect patterns that would not be visible if only looking at a single frame. The resulting classification should be more 
accurate than using either technique alone.

4. What are the advantages of building an RNN using dynamic_rnn() rather than static_rnn()?

Ans: Dynamic_rnn() is more computationally efficient than static_rnn() because it allows for variable-length inputs and does not 
require the user to specify the input sequence length prior to model training.
Dynamic_rnn() allows for greater flexibility in constructing the model, as it allows for the creation of more complex recurrent 
architectures such as bidirectional RNNs and stacked RNNs.
The dynamic_rnn() function also allows for efficient backpropagation through time, allowing for faster training and better 
performance on time series data.

get_ipython().set_next_input('5. How can you deal with variable-length input sequences? What about variable-length output sequences');get_ipython().run_line_magic('pinfo', 'sequences')

Ans: For variable-length input sequences, one can use padding or truncation. Padding involves adding an appropriate value (e.g. 
zeros) to the beginning or end of shorter sequences, so that all inputs have the same length. Truncation involves discarding 
information from the end of longer sequences, so that all inputs have the same length.

For variable-length output sequences, one can use a technique called bucketing. Bucketing involves grouping sequences of similar 
lengths together, and then training a separate model for each group. This allows the model to learn different patterns for each 
group and thus produce variable-length output sequences.

get_ipython().set_next_input('6. What is a common way to distribute training and execution of a deep RNN across multiple GPUs');get_ipython().run_line_magic('pinfo', 'GPUs')

Ans: One common way to distribute training and execution of a deep RNN across multiple GPUs is to use a data-parallel approach.
This involves splitting the data across different GPUs, and then training the network on each GPU in parallel. The results from
all GPUs are then aggregated together and used to update the model parameters. This approach allows for much faster training and
execution of deep RNNs, since the workload is distributed across multiple GPUs.

