pipeline {
    agent any
        stages {
            stage('Clone Git') {
                steps {
                    git 'https://github.com/chakradhar06/IMT2020007_Jenkins.git'
                }
            }
            stage('Build Code') {
                steps {
                    sh "/usr/bin/python3 perfectsquare.py"
                }
            }
            stage('Test Code') {
                steps {
                    sh "/usr/bin/python3 test.py"
                }
            }
            stage('Monitoring') {
                steps{
                    echo "This step is monitoring"
                }
            }
        }
}

