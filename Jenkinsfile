pipeline {
    agent {
            docker {
                image 'python:3.10-slim'
                reuseNode true
            }
    }
    envrionment {
        VERIF_URL = credentials('vera_transalation_verification_url')
    }
    stages {
        stage ('Validation') {
                steps {
                    sh "python3 validation.py -b ${env.BRANCH_NAME} -u $VERIF_URL"
                }
            }
    }
    
}