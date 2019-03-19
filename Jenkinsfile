node('slave1'){
    currentBuild.result = "SUCCESS"
    stage('Printing hello world'){
        sh 'echo "Hello World"'
    }
node('slave2'){
    currentBuild.result = "SUCCESS"
    stage('Printing hello world'){
        sh 'echo "deploy ok"'        
    }
