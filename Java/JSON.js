{ "userID": 1, "id": 1, "title": "Test title", "status": { "complated": false } }
JSON.parse()#джейсон строка распарсив получаем файл джава
{
    userId: 1,
        id: 1,
            title: 'Test title',
                status: {
        complated: false,
    }

}

JSON.stringify() конвертация объекта в джейсон

const post = {
    title: 'My post',
    likesQty: 5
}
undefined
post
{ title: 'My post', likesQty: 5 }
JSON.stringify(post)
'{"title":"My post","likesQty":5}'

const postStringified = JSON.stringify(post)
undefined
JSON.parse(postStringified)
{ title: 'My post', likesQty: 5 }