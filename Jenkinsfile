node('slave1'){
    currentBuild.result = "SUCCESS"
    stage('Printing hello world'){
        sh 'echo "Hello World"'
    }stage
    node('slave2'){
        curl -X POST --data-urlencode "payload={\"channel\": \"#webhooks\", \"username\": \"ynonye\", \"text\": \"Deploy succseded.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/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
            }    
}
