/*
<input level="1" name="power[]" value="1" type="checkbox" >
 */
$("input[type='checkbox']").on('click',function(){
    var obj = $(this);
    var chk = $("input[type='checkbox']");
    var count = chk.length;
    var num = chk.index(obj);
    var level_top = level_bottom = chk.eq(num).attr('level');
    for (var i=num-1; i>=0; i--)
    {
        //向上查找
        var le = chk.eq(i).attr('level');
        if(eval(le) < eval(level_top))
        {
            chk.eq(i).prop("checked",true);
            var level_top = level_top-1;
        }
        if(eval(le) == 0) break;
    }
    for (var j=num+1; j<count; j++)
    {
        //向下查找
        var le = chk.eq(j).attr('level');
        if(eval(le) == eval(level_bottom)) break;
        if(eval(le) > eval(level_bottom)){
            var tag = obj.prop('checked');
            chk.eq(j).prop("checked",tag);
        }
    }
    jQuery.uniform.update(chk);
});