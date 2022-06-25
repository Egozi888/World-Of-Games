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
                stage('Image_Run') {
            steps {
                echo "- - - - - - - Docker Image Run - - - - - - - - "
                sh "docker run -p 5000:5000 -d flask"
            }
        }
    }
}
