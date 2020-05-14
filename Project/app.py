import numpy as np
import pickle
import tensorflow as tf
import model
import sys

# Load in data structures
with open("data/wordList.txt", "rb") as fp:
    wordList = pickle.load(fp)
wordList.append('<pad>')
wordList.append('<EOS>')

# Load in hyperparamters
vocabSize = len(wordList)
batchSize = 24
maxEncoderLength = 15
maxDecoderLength = 15
lstmUnits = 112
numLayersLSTM = 3

# Create placeholders
encoderInputs = [tf.placeholder(tf.int32, shape=(None,)) for i in range(maxEncoderLength)]
decoderLabels = [tf.placeholder(tf.int32, shape=(None,)) for i in range(maxDecoderLength)]
decoderInputs = [tf.placeholder(tf.int32, shape=(None,)) for i in range(maxDecoderLength)]
feedPrevious = tf.placeholder(tf.bool)

encoderLSTM = tf.nn.rnn_cell.BasicLSTMCell(lstmUnits, state_is_tuple=True)
#encoderLSTM = tf.nn.rnn_cell.MultiRNNCell([singleCell]*numLayersLSTM, state_is_tuple=True)
decoderOutputs, decoderFinalState = tf.contrib.legacy_seq2seq.embedding_rnn_seq2seq(encoderInputs, decoderInputs, encoderLSTM,
                                                            vocabSize, vocabSize, lstmUnits, feed_previous=feedPrevious)

decoderPrediction = tf.argmax(decoderOutputs, 2)

# Start session and get graph
sess = tf.Session()
#y, variables = model.getModel(encoderInputs, decoderLabels, decoderInputs, feedPrevious)

# Load in pretrained model
saver = tf.train.Saver()
saver.restore(sess, tf.train.latest_checkpoint('models'))
zeroVector = np.zeros((1), dtype='int32')

def pred(inputString):
    inputVector = model.getTestInput(inputString, wordList, maxEncoderLength)
    feedDict = {encoderInputs[t]: inputVector[t] for t in range(maxEncoderLength)}
    feedDict.update({decoderLabels[t]: zeroVector for t in range(maxDecoderLength)})
    feedDict.update({decoderInputs[t]: zeroVector for t in range(maxDecoderLength)})
    feedDict.update({feedPrevious: True})
    ids = (sess.run(decoderPrediction, feed_dict=feedDict))
    return model.idsToSentence(ids, wordList)


print('\n\n\n\n\n\n\n\n\n\n\n')
print("Gavin 2.0: Hey, I'm Gavin's virtualized brain, talk to me by typing something below.")
user_input = input("What would you like to say to Gavin 2.0?  -->  ")
print("Gavin 2.0: " + pred(user_input))
while True:
    user_input = input("-->  ")
    if user_input != "Quit":
        if(user_input == ""):
            print("Enter Quit to quit.")
            continue
        else:
            print("Gavin 2.0: " + pred(user_input))
    else:
        print("Alright, Cya")
        sys.exit(0)