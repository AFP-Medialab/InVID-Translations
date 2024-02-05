pipeline {
    agent {
            docker {
                image 'python:3.10-slim'
                reuseNode false
            }
    }
    environment {
        VERIF_URL = credentials('vera_transalation_verification_url')
    }
    stages {
        stage ('Validation') {
                steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh "pip install requests"
                        sh "python3 validation.py -b ${env.BRANCH_NAME} -u $VERIF_URL"
                    }
                    
                }
            }
    }
    
}