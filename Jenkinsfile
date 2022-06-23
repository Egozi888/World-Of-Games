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
                stage('Image_Build') {
            steps {
                echo "- - - - - - - Docker Image Build - - - - - - - - "
                sh "docker build -t flask ."
            }
        }
    }
}