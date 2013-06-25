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
> __I__ can'__t__ se__e__ th__e__ woo__d__ fo__r__ th__e__ tree__s!__

you will get
> ItEeDrEs!81

as your passphrase.

##Installation
just download or clone the PhraseToPass.py

##Usage
To run the PhraseToPass, type:
> python3 PhraseToPass.py

or make _PhraseToPass.py_ executable and type:
> ./PhraseToPass.py
