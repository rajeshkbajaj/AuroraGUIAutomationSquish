# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names

@Given("I am changing Theme from drak to light")
def step(context):
    # test.warning("TODO implement some precondition is met")
    mouseClick(waitForObject(names.mainWindow_button_Button_3), 16, 25, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_2), 17, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_3), 23, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_button_Button_4), 23, 21, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 351, 62, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 288, 55, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_border_Rectangle_2), 878, 454, Qt.LeftButton)

@Given("another precondition")
def step(context):
    test.warning("TODO implement another precondition")

@When("some action is performed")
def step(context):
    test.warning("TODO implement some action is performed")

@Then("the results should be as expected")
def step(context):
    test.warning("TODO implement the results should be as expected")

@Then("some other testable outcome is achieved")
def step(context):
    test.warning("TODO implement some other testable outcome is achieved")

@Given("The Application was Launched")
def step(context):
    # test.warning("TODO implement The Application was Launched")
    startApplication("MedtronicUI")
