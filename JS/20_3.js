function solution(strArr) {
    let answer = {};
    strArr.forEach((item) => {
        answer[item.length] = answer[item.length] ?? [];
        answer[item.length].push(item);
    });
    let lenlist = Object.values(answer).map((i) => i.length);
    return Math.max(...lenlist);
}
