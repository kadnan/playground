import os
import glob
import mimetypes
from shutil import copyfile


def mv_lines(source_directory, line_limit, pattern, extension, destination_directory):
    """
        Move files to other destination based on number of lines in a text file
    """
    os.chdir(source_directory)
    files = []
    for fn in glob.glob('*.' + extension):
        file_path = os.path.join(rootdir, fn)
        # Is it a text file?
        m_type = mimetypes.guess_type(file_path)

        if m_type[0] == 'text/plain':
            with open(fn) as f:
                file_lines = len(f.readlines())

                if pattern == '>':
                    if file_lines > line_limit:
                        files.append(fn)

                if pattern == '<':
                    if file_lines < line_limit:
                        files.append(fn)

                if pattern == '=':
                    if file_lines == line_limit:
                        files.append(fn)
    if len(files) > 0:
        [copyfile(source_directory + '/' + f, destination_directory + '/' + f) for f in files]


rootdir = '/path/to/source'
destdir = 'path/to/destination'

# Example
mv_lines(rootdir, 5000, '>', 'txt', destdir)
