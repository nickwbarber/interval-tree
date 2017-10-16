import gate
import intervaltree

test_file = "/home/nick/temp/test.xml"

annotation_file_obj = gate.AnnotationFile(test_file)
twn = annotation_file_obj.get_text_with_nodes()

tree = intervaltree.IntervalTree(
    annotation_file_obj.iter_annotations(),
    lambda x: x.get_start_node(),
    lambda x: x.get_end_node(),
)

print(
    tree.get_root().get_data().get_text(twn)
)
