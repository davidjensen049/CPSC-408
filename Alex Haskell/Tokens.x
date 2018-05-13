{
module Main (main) where
}

%wrapper "basic"

$digit = 0-9			-- digits
$alpha = [a-zA-Z]		-- alphabetic characters

tokens :-

  $white+				;
  "--".*				;
  let					{ \s -> Let }
  in					{ \s -> In }
  $digit+				{ \s -> Int (read s) }
  [\=\+\-\*\/\(\)]			{ \s -> Sym (head s) }
  $alpha [$alpha $digit \_ \']*		{ \s -> Var s }

{
-- Each action has type :: String -> Token

-- The token type:
data Token =
	Let 		|
	In  		|
	Sym Char	|
	Var String	|
	Int Int
	deriving (Eq,Show)

main = do
  s <- getContents
int x = 1;
int y = 2;

return x+(5*y);

  print (alexScanTokens s)
}
