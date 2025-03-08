import os

def find_cpp_files(directory):
    cpp_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.cpp'):
                # Add the full path of the .cpp file
                cpp_files.append(os.path.join(root, file))
    return cpp_files

def generate_cmake_add_library(cpp_files):
    # CMake command for adding the static library
    cmake_command = 'add_library(soloud STATIC\n\n'
    
    for file in cpp_files:
        cmake_command += f'    {file}\n'
    
    cmake_command += ')'
    return cmake_command

def main():
    # Specify the directory to search for .cpp files
    directory = './'  # Modify this with your directory path

    # Find all .cpp files in the directory
    cpp_files = find_cpp_files(directory)

    # Generate the CMake command
    cmake_command = generate_cmake_add_library(cpp_files)

    # Print the CMake command
    print(cmake_command)

if __name__ == '__main__':
    main()
