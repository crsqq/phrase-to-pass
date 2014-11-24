# phrase-to-pass
**phrase-to-pass** is a simple tool to convert phrases to secure passwords

#About

##How does it work?

You have to enter a phrase (which you can remember easily). If the given phrase
is long enough, the program will generate a fairly secure passphrase.  It uses
the last character from every word, special characters are taken into
account. To make the passphrase even longer and more secure, the squared sum of
all yet existing characters will be appended.  The following example
illustrates the password generating process:

Given the phrase:
> I can't see the wood for the trees!

you will get
> ItEeDrEs!81

as your passphrase.

##Installation
just download or clone the PhraseToPass.py

##Usage
Pass your phrase via command line argument:

`python3 PhraseToPass.py I can't see the wood for the trees!`

or make PhraseToPass.py executable and:

`./PhraseToPass.py I can't see the wood for the trees!`
