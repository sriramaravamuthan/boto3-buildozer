# boto3-buildozer

[Refer Buildozer Installation ](https://buildozer.readthedocs.io/en/latest/installation.html)
```
pip3 install --user --upgrade buildozer

sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv
```

# Commands to run
Check out the project and run below command

Below takes some time and downloads all necessary NDK, SDK and tool chains
```
buildozer init
```

# When requirements is updated
buildozer android update 

# To deploy to connected device
buildozer android deploy run 

# To see logs
buildozer android deploy run logcat
