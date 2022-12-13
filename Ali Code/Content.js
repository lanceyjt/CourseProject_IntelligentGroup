let willSmithImages = 
[
    "https://www.lovethispic.com/uploaded_images/80903-Funny-Will-Smith.jpg",
    "https://media1.popsugar-assets.com/files/thumbor/BrT6JuS0boRe5dXrvkKQ4rzGNME/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2019/02/10/215/n/1922283/ad358e065c60f5ad56e7e8.61160339_/i/Funny-Tweets-About-Smith-Genie-Aladdin-Trailer.jpg",
    "https://observatoriodocinema.uol.com.br/wp-content/uploads/2020/07/will-smith-foto.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/TechCrunch_Disrupt_2019_%2848834434641%29_%28cropped%29.jpg",
    "https://i0.wp.com/mixdeseries.com.br/wp-content/uploads/2018/07/will-smith-4-e1534947669898.jpg?fit=871%2C499&ssl=1",
    "https://conteudo.imguol.com.br/c/entretenimento/e3/2020/07/09/will-smith-1594320007897_v2_450x337.jpg",
];

const imgs = document.getElementsByTagName("img");
for (let i = 0; i < imgs.length; i++) {
 const randomImg = Math.floor(Math.random() * willSmithImages.length);
 imgs[i].src = willSmithImages[randomImg];
}

const headers = document.getElementsByTagName("h1");
for (let i = 0; i < headers.length; i++) {
 headers[i].src = "Ali is Awesome";
}