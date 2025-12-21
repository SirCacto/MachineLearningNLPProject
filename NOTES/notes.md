############# Random notes for creator to remember things. You can ignore this file! #############

As of now:

Logistic Regression Model: 0.9865 accuracy, 0.9831 MCC

Bert: 1.0 accuracy, 1.0 MCC

LSTM: 0.8610 accuracy, 0.8307 MCC

There's a new Bert model saved in drive./ Same model but trained again so maybe different? UPDATE: This will be true of LogReg as well.

LTSM should have trained but we mightve closed out of it on colab

LogReg also has a drive folder now.

OK SO IN SHORT:

The Colab code is more updated than the VSCode Colab code.

All 3 models have updated versions saved in drive.

LSTM and LogReg had their tests calculated during the Colab code, while BERT has its calculated in test_model.py.

I trained a new model of Bert and saved it in Drive from Colab. It was trained exactly the same way so I have no clue if its accuracy and whatnot will be the same. Probably is, just ran the code again. That version is in Drive, and not on the computer (the latter of which has its score listed on this file as of now).

These notes were written 12/20/2025 at 4:50 PM.

As of 12/21/25 at 1 PM, the Colab code saved locally is the updated version. Haven't run it yet but should be good.



Ok so as of 12/21/25 at 6:42 PM, the VSCode Colab code doesn't have any working test code for the 4 specific tests. HOWEVER, they are on Colab online. They're messy, so I'll copy them over and clean them when I have time.








DATA!!!!


BERT GUESSES:

Headline: The central bank raised interest rates to combat inflation today.
Prediction: business (95.70% confidence)
Headline: Bleepity bloopity blop! Blorg blorg blop.
Prediction: entertainment (90.57% confidence)
Headline: Ar ar ar ar ar ar ar ar.
Prediction: politics (39.22% confidence)
Headline: Football
Prediction: entertainment (30.08% confidence)



LogReg Guess Ar: sport (33.25% confidence)
LogReg Guess Bank: business (69.75% confidence)
LogReg Guess Bleep: sport (33.25% confidence)
LogReg Guess Football: sport (52.93% confidence)



LSTM Guess Ar: sport (99.65% confidence)

LSTM Guess Bank: sport (93.55% confidence)

LSTM Guess Bleep: sport (99.65% confidence)

LSTM Guess Football: sport (99.61% confidence)





If you're reading this, hello! My notes are messy, but they're sure to become something beautiful on my report.
