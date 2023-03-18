
$('.catalog__price').text((i, text) => {
    const [ price, currency ] = text.split(' ');
    return `${(+price).toLocaleString()} ${currency}`;
  });

$('.product-price').text((i, text) => {
  const [ price, currency ] = text.split(' ');
  return `${(+price).toLocaleString()} ${currency}`;
});
$('.sum_price-number').text((i, text) => {
  const [ price, currency ] = text.split(' ');
  return `${(+price).toLocaleString()} ${currency}`;
});