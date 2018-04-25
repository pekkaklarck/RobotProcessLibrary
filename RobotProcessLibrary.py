import os
import sys
import tempfile

from robot.api import logger
from robot.libraries.Process import Process
from robot.utils import html_escape, plural_or_not as s


class RobotProcessLibrary(Process):

    def run_robot_process(self, *sources, **config):
        if 'outputdir' not in config:
            config['outputdir'] = tempfile.mkdtemp()
        command = [sys.executable, '-m', 'robot']
        for name in config:
            command.extend(['--%s' % name, config[name]])
        command += sources
        result = self.run_process(*command, stderr='STDOUT')
        logger.info(self._format_robot_output(result.stdout, config), html=True)
        if result.rc not in range(251):
            raise AssertionError('Robot Framework did not start correctly or '
                                 'execution was terminated (rc %s).'
                                 % result.rc)
        if result.rc != 0:
            raise AssertionError('%s failure%s in Robot Framework execution.'
                                 % (result.rc, s(result.rc)))

    def _format_robot_output(self, output, config):
        output = html_escape(output)
        log = os.path.join(config['outputdir'], config.get('log', 'log.html'))
        report = os.path.join(config['outputdir'], config.get('report', 'report.html'))
        output = output.replace(log, "<a href='file://%s'>%s</a>" % (log, log))
        output = output.replace(report, "<a href='file://%s'>%s</a>" % (report, report))
        return output
