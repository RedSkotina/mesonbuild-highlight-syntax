import logging
import os
import json
import inspect
import ast
from cliff.command import Command

class MParserVisitor(ast.NodeVisitor):
    def visit_Assign(self, node):
        self.generic_visit(node)
        
class Extract(Command):
    "A extract command that extract data from the meson build installation to json file."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = Command.get_parser(self, prog_name)
        parser.add_argument('-o', '--output', type=str, default = 'data.json', help='specify output json filename')
        parser.add_argument('meson_dir', type=str, default = '',  nargs='?', help="specify the meson build system installation directory")
        return parser
        
    def take_action(self, parsed_args):
        try:
            import mesonbuild.mparser as mparser
            import mesonbuild.interpreterbase as interpreterbase
        except ImportError:
            raise ImportError('<meson not installed>')
        if parsed_args.meson_dir == '':
            parsed_args.meson_dir = os.path.dirname(inspect.getfile(mparser))
        self.log.info('Extract data from {}'.format(parsed_args.meson_dir))
        
        self.extract_keywords(mparser)
        
        data = []
        #self.app.stdout.write('hi!\n')
        self.log.debug('Data writed to {}'.format(parsed_args.output))
        with open(parsed_args.output, 'w') as fh:
            json.dump(data, fh, indent=4, sort_keys=True)
            
    def extract_keywords(self, mparser):
        self.log.debug('extract_keywords')
        mparser_src = inspect.getsource(mparser)
        root_node = ast.parse(mparser_src)
        MParserVisitor().visit(root_node)
        
    def extract_some(self):
        self.log.debug('extract_keywords')
