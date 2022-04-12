db.createUser({
    user:"readonly",
    pwd:"password",
    roles: [{
        role:"readWrite",
        db:"quiz"
    }]
})