# github-package.py

'''Set up Github on Linux

If have not set up git on linux.
$ git config --global user.name "<Your Name>"
$ git config --global user.email <your email address>

if you are using atom editor:
$ git config --global core.editor "atom --wait"

To check details:
$ git config --list

1. Checking for existing SSH Keys
$ ls -al ~/.ssh

2. "Generating Your SSH Public Key"
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
id_rsa and rd_rsa.ub files should be created in .ssh folder

3. Adding your SSH key to the ssh-agent
$ eval "$(ssh-agent -s)"
> Agent pid 59566

$ ssh-add ~/.ssh/id_rsa

4. Adding a new SSH key to your github account via "setting" -> "SSH and GPG Keys"

5. Testing your SSH connection
$ ssh -T git@github.
If problems see a link below:
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/testing-your-ssh-connection


'''
