# aws-openquake
Python (Boto3) script which installs, runs and downloads results from seismic hazard and risk software (OpenQuake Engine) on Amazon Web Services EC2.

Setup
-----

Install Python modules by running:
```
$ pip install -r requirements.txt
```

Add your AWS keys to ~/.aws/credentials:
```
[default]
aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
```

Add AWS region (for example, Sydney `ap-southeast-2`) to ~/.aws/config:
```
[default]
region = ap-southeast-2
```

Configure OpenQuake job
-----------------------
Edit OpenQuake Engine job files (by default runs example SimpleFaultSourceClassicalPSHA job):
```
$ ls openquake/
README.txt                  job.ini                     source_model.xml
gmpe_logic_tree.xml         report.rst                  source_model_logic_tree.xml
```

Consult the OpenQuake documentation for more details: http://www.globalquakemodel.org/openquake/support/documentation/engine/.

Run the script
--------------
Running `launch_aws.py` will:
- setup the AWS infrastructure (security group, SSH key, and EC2 instance)
- upload `openquake/` directory to instance (including job files)
- execute `oq-engine` with `openquake/job.ini`
- download `oqdata` directory with results 
```
$ python launch_aws.py
setting up
deploying
2016-04-25 06:22:26.213652: installing openquake
2016-04-25 06:24:13.789055: running openquake
2016-04-25 06:24:48.001661: finished
downloading results
tearing down
```

This should result in an `oqdata-openquake-...` directory:
```
$ ls
README.md                   oqdata-openquake-1461565289 scp.pyc
launch_aws.py               test_launch_aws.py          webserver.py
master_script.sh            requirements.txt            openquake
openquake
```
