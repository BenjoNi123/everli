<?php

class Path{

    public $currentPath;

    public function __construct($path)
    {
        $this->currentPath = $path;
    }

    public function cd($cdPath)
    {
        if($cdPath[0]=="/")
        {
            $this->currentPath = $cdPath;
            return true;
        }


        $explodedCDPath = explode("/", $cdPath);
        $explodedRealPath = explode("/", $this->currentPath);

        $goBack="..";
        $goBackCount = 0;
        foreach($explodedCDPath as $key => $part)
        {
            if($part==$goBack)
            {
                $goBackCount++;

                unset($explodedCDPath[$key]);
            }   
        }

        $explodedRealPathReverse = array_reverse($explodedRealPath);

        $counter = 0;

        foreach ($explodedRealPathReverse as $key => $rev)
        {
            if($counter < $goBackCount)
            {
                unset($explodedRealPathReverse[$key]);
            }

            $counter++;
        }

        $explodedRealPath = array_reverse($explodedRealPathReverse);

        $newRealPathArray = array_merge($explodedRealPath, $explodedCDPath);
        $newRealPath = implode("/", $newRealPathArray);

        $this->currentPath = $newRealPath;

    }


}


$path = new Path('/a/b/c/d');
$path->cd('..');
echo $path->currentPath;
