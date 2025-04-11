# Decoding AI Jargons

## Transformers

What is a transformer?? no… its not your childhood memory of a car that turns into a robot, but it’s the brain behind the chatbot you use daily. Now this “***Attention is All You Need***“.

## Encoder

An encoder is a translator which is used by the AI systems to translate your language into embeddings that the AI model understands.

## Decoder

Its the same translator but it translate the gibberish output from the AI model to the language in which you expect it to be in.

## Vectors

Its magnitude with direction. YES the same old physics definition but here it give you the distance between the next word which might probably be the next possible word in a auto complete sentence

## Embeddings

Its basically a dictionary which consists of words, images, or videos in a form that computers can process

## Positional Encoding

Sometimes altering the in a sentence can change the entire meaning of the sentence for example Dollar is expensive than Rupee make sense but what if Rupee is expensive than Dollar “hoping to see this come true one day” but as of now it does not make sense. So the positional encoding ensures this and give the sentence an proper meaning.

## Semantic Meaning

This is used to basically understand the meaning of the word in a particular sentence

Let us understand this with an example, The **bat** flew out of the cave; Batsman hit the ball with a **bat**. Here bat the word is same in both the cases but has a different meaning when its used in different sentences. So Semantics help in understanding the context of the word in a sentence.

## Self-Attention

Its the tokens talking to each other to adjust the embeddings accordingly. Example "***bank***" in “river *bank*” vs “money *bank*”

## SoftMax

Its a function used in the output layer of Neural Network that is used to predict the output based on the highest probability values

## Multi-Head Attention

Process in which multiple self-attention mechanisms runs in parallel, improving the model’s ability to understand complex relationships in the text. Just imagine a Airplane, what did you imagine it as a white object, blue sky, landing runway, etc. The same processing if it happens with a AI system then that is Multi-Head Attention.

## Temperature

One word answer : **Randomness Controller.** Lower the value more deterministic, Higher the value more creative. Ranges typically between (0 - 2 )

## Knowledge Cutoff

The last date till the AI Model (a LLM) is been trained on data.

## Tokenization

The process of breaking down text into pieces

## Vocab Size

Its the total size of unique tokens that a LLM understands.