#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import string
import wordcloud

"""
Module to clean tweets and generate cloud
"""

class TwitterModule:

    def __init__(self):
        self.file_path=os.path.abspath(__file__)
        self.punctuations=string.punctuation
        self.digits=string.digits
        self.corpus=""

    def prepare_corpus(self, file_name):
        """
        Method to prepare corpus
        :param file_name: 
        :return: 
        """
        path = self.file_path
        with open(file_name, 'r') as file_reader:
            text = file_reader.read()
        self.corpus=text
        self.remove_punctuations()
        self.word_cloud()

    def remove_punctuations(self):
        """
        Method to remove punctuation
        :return: 
        """
        punctuation_translate=string.maketrans(self.punctuations,len(self.punctuations)*" ")
        self.corpus.translate(punctuation_translate)
        print self.corpus

    def word_cloud(self):
        """
        Method to generate cloud
        :return: 
        """
        wc = wordcloud.WordCloud(min_font_size=10, max_font_size=40,
                                 background_color='white').generate(self.corpus)
        wc.to_file('cloud.png')




