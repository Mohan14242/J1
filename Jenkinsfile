    // Define the 'names' function within the pipeline block
    def names(Map maps) {
        def prod_deploy = maps.prod_deploy
        def environment = maps.environment
        def choice = maps.choice
        def password = maps.password
        
        stage("printing") {
            steps {
                script {
                    echo "Enable debug mode: ${prod_deploy}"
                    echo "Environment: ${environment}"
                    echo "Browser: ${choice}"
                    echo "Database Password: ${password}"
                }
            }
        }
    }

