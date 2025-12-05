pipeline{
    agent: any
    environment {
        AWS_ID = "189326461630"
        REGION = "us-east-1"
        IMAGE = "${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/hello-devops:latest"
    }

    stages: {
        stage("Get code from github"){
            steps{
                sh "git https://github.com/Thara8885/devops-mini-project.git"
            }
        }
        stage("Build docker image"){
            steps{
                sh 'docker build -t hello-devops ./app'
            }
        }
        stage("Login to ECR"){
            steps{
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 189326461630.dkr.ecr.us-east-1.amazonaws.com' 
            }
        }
        stage("Push image to ECR"){
            steps{
                sh '''
                docker tag hello-devops:latest $IMAGE
                docker push $IMAGE
                '''
            }
        }
        stage("Deploy to kubernetes from ansible"){
            steps{
                sh 'ansible-playbook ansible/deploy.yaml'
            }
        }
    }
}