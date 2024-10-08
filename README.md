
# Welcome to your CDK Python Prompt Flow project!

This particular CDK construct is a demo to use CDK to create a simple PromptFlow that contains Input Node connecting to the Output Node. This is demo example that highlights 
how PromptFlow in Bedrock can be created with Infrastructre as a Code. Here are the instructions to follow:

#Step1: Clone this GitHub repository to your dev environment. Follow the steps here:
https://learn.microsoft.com/en-us/visualstudio/version-control/git-clone-repository?view=vs-2022

#Step2: Configure and Deploy the CDK
```
$ cdk synth cdk_promptflow_inputoutput_iam
$ cdk deploy cdk_promptflow_inputoutput_iam
```

This is how the sample PromptFlow will be rendered in the Bedrock Flow console.
<img width="568" alt="Screenshot 2024-09-02 at 13 32 37" src="https://github.com/user-attachments/assets/1a69f8d4-642e-4261-8ea7-d70e4557b2df">


#Step3: Once you are done reviewing the prompt flow in the Bedrock Console of AWS, then don't forget to destroy
```
$ cdk destroy cdk_promptflow_inputoutput_iam
```

# Instructions for CDK development with Python #

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
