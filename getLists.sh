for page in $(seq 1 21) ; do
    curl "http://hobbyking.com/hobbyking/store/uh_listCategoriesAndProducts.asp?cwhl=XX&pc=85&idCategory=86&curPage=$page&v=&sortlist=&sortMotor=&LiPoConfig=&CatSortOrder=desc" > page-$page 
done
