function chunk(arr: any[], size: number): any[][] {
    let res = []
    for(let i = 0; i<arr.length;i+=size) {
        res.push(arr.slice(i,i+size))
    }
    
    return res

};
