function isEmpty(obj: Record<string, any> | any[]): boolean {
    if(Array.isArray(obj)){
        if(obj.length == 0) {
            return true
        }else {
            return false
        }
    } else {
        if(Object.keys(obj).length == 0) {
            return true
        }else {
            return false
        }
    }

};