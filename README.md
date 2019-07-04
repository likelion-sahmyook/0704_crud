# 0704_crud
# Jquery CRUD
<pre><code>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
     integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"></script>
</code></pre>
        
# 삭제확인 컨펌 스크립트

<pre><code>
  <script>
       $('#delete').click(function () {
           if (confirm('Are you sure?') == true) {
           } else {
               return false;
           }
      });
   </script>
</code></pre>
