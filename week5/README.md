### 要求三：SQL CRUD
- 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

    - 圖1：使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。

        ![ ](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/228d1d12-c50c-403d-8fe5-c0b1ae16494b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T064027Z&X-Amz-Expires=86400&X-Amz-Signature=9727ade533b84ece84b6942a3d594872bc7468a7fc2c8f22429b703b003c4014&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
        ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dbbd281b-7d32-4215-a8a4-890869702577/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T064237Z&X-Amz-Expires=86400&X-Amz-Signature=0fd2073a1c37325c81c01ea4834352632e6f4cd0836b31865161e43bc1503980&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
    - 新增至少 4 筆隨意的資料。
        ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6279c8c0-27d0-46cd-9383-8d5845f022f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T072503Z&X-Amz-Expires=86400&X-Amz-Signature=f46a4069e2017bbfe81a7ca65860351c8805b7996e420d3405ccf99e9777a338&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
        ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/169c58cc-1b4a-4bbc-9b46-708e8bd67082/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T072540Z&X-Amz-Expires=86400&X-Amz-Signature=2ee898973740c0f39d7c8f5bdccc527e2ad3d9e72f468d07b3faf27dd6bc5f6b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

    ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/169c58cc-1b4a-4bbc-9b46-708e8bd67082/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074706Z&X-Amz-Expires=86400&X-Amz-Signature=be657aab6c35955b6a8b91dfdcfa2f2a9e37f5b2052576eddd7538a57d59a6d7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/337933ea-7114-430c-b659-1345a584fc03/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074605Z&X-Amz-Expires=86400&X-Amz-Signature=ce842f989368999122607fa96b2b48fe7ad122920503ee6cc526bdfb799c30b6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

    ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cefc49ab-4def-46e8-8765-23a31f0958e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074250Z&X-Amz-Expires=86400&X-Amz-Signature=5c86819f59366376ff9fe7888967e9fbb20a0f9e6661e54c31ab34dae1da7d53&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2661d729-ffc1-4580-b19f-41170da32aee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074829Z&X-Amz-Expires=86400&X-Amz-Signature=3f6b70ec342d7e6f398c2f41478331cb03de861fae21350e657adbcefd3a5372&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a730de36-ce95-40f6-8d53-c41d15c01cec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074906Z&X-Amz-Expires=86400&X-Amz-Signature=da3fc7b5fc334faa2adf5803266e3bb005ea1540687588a5733d841db3aa93a9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cc0a43fc-5ee0-40ac-b3fa-5c9ad8ade605/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T074935Z&X-Amz-Expires=86400&X-Amz-Signature=e18d1d1e039e08443984e63de7f779271ff9b6b9f12051045ead56d374692887&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 要求四：SQL Aggregate Functions
利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令：
- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
    
    ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2d0485e0-dabd-4349-a2c0-39ef0a7e1cea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T075634Z&X-Amz-Expires=86400&X-Amz-Signature=5393e99d8e5ae5ac8bf4c6fc67c3aedf2f96418eba317bc83574729da8662c3d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/53375e04-0ee4-4341-bcea-437bb502fe16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T075701Z&X-Amz-Expires=86400&X-Amz-Signature=35dd35b6abb0bb1fac95cfd58659afeb6d04d8f1da471f7c2ebb622c70374e5d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e93c83e4-b678-49c3-9063-d1e7671c2d60/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T075727Z&X-Amz-Expires=86400&X-Amz-Signature=938bf2ef2e2eaaf4d28436b5329440d2051885415a4fd246647b77201e5d6222&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 要求五：SQL JOIN (Optional)
- 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b5613d77-8f94-4ab2-9545-f222fd80942a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T075915Z&X-Amz-Expires=86400&X-Amz-Signature=1eb741a4e298b15556d0a57663106a40df7e1f4f779315b6ef9fe524e8612061&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0e550a7c-d0f5-43be-b628-9f53fef5c055/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T075954Z&X-Amz-Expires=86400&X-Amz-Signature=df85b0d2286142fd02ce6565b843ec9873e0047745ae317059a5d307fdae7f00&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dcea8644-a6cf-450c-9600-386064e6a7d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T080028Z&X-Amz-Expires=86400&X-Amz-Signature=15841509c29086b45150cf9de721510aefbfd865bab6a9c3962f671fdbc89609&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f21fc238-afed-40b1-aa0f-dcb12b9194de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220126T080107Z&X-Amz-Expires=86400&X-Amz-Signature=904ae64388d221d157482d570888512136a6487e6b3c9315c90a578eafcade9c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
