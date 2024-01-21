pipeline{
    agent None

    stages{
        stage('build'){
            agent{
                label 'ansible'
            }
                script{
                    git clone https://github.com/Mohan14242/jenkins2.git
                    cd jenkins 
                    ansible -i inventory.ini all -m ping
                }
            }
        }
        stage("testting stage"){
            steps{
                script{
                    echo "this is the chiru who are you"
                }
            }
        }
    }
}
