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
                        validate_log = sh(script:"python3 validation.py -b ${env.BRANCH_NAME} -u $VERIF_URL", returnStdout: true).trim()
                    }
                    slackSend channel: 'medialab_builds', message: "Job: ${env.JOB_NAME} - ID: ${env.BUILD_ID} \n Validation logs:  ${validate_log}", tokenCredentialId: 'medialab_slack_token'
                    
                }
            }
    }
    
}