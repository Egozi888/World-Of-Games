pipeline {
    agent any

    stages {
        stage('Initial_stage') {
            steps {
                sh '''
                    ls -la
                    '''
            }
        }
                stage('Disk-space') {
            steps {
                echo "- - - - - - - Disk-Space Stage - - - - - - - - "
                sh ' ls -l'
            }
        }
    }
}