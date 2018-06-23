from selenium import webdriver
import time

def before_feature(context, feature):
	context.dr = webdriver.Firefox()

def after_feature(context, feature):
	context.dr.close()
