#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (None, None)
    return (len(sentence), sentence[None])
