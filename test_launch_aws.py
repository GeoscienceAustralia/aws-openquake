import boto3
from moto import mock_ec2
from launch_aws import Launcher
import unittest
import mock


class TestAWSLaunch(unittest.TestCase):
    @mock_ec2
    def test_setup(self):
        ec2 = boto3.resource('ec2')

        launcher = Launcher()

        with mock.patch('__builtin__.open', mock.mock_open(), create=True) as m:  # mock file creation
            launcher.setup()

        # created keypair file
        assert m.call_args == mock.call(launcher.timestamp + '.pem', 'w')
        # created created AWS SSH keypair
        assert launcher.timestamp in [k.name for k in list(ec2.key_pairs.all())]
        # created security group
        assert launcher.timestamp in [k.group_name for k in list(ec2.security_groups.all())]
        # created instance
        assert launcher.instance.id in [x.id for x in list(ec2.instances.all())]

    @mock_ec2
    def test_teardown(self):
        ec2 = boto3.resource('ec2')

        launcher = Launcher()

        with mock.patch('__builtin__.open', mock.mock_open(), create=True):  # mock file creation
            launcher.setup()

        with mock.patch('os.remove') as m:
            launcher.teardown()

        assert m.call_args == mock.call(launcher.timestamp + '.pem')
        assert launcher.timestamp not in [k.name for k in list(ec2.key_pairs.all())]
        assert launcher.timestamp not in [k.group_name for k in ec2.security_groups.all()]
        assert [i for i in list(ec2.instances.all()) if i.id == launcher.instance.id][0].state['Name'] == 'terminated'

    # test deploy
    # mock web and ssh
